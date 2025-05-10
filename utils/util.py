import pandas as pd
import duckdb


def parse_challenge_response(response: list) -> pd.DataFrame:
    """
    given the API response (list of all players who completed the challenge)
    we will make a DataFrame and set the index to the player name
    """
    df = pd.json_normalize(response)
    df = pd.json_normalize(df['items'][0])
    return df


def clean(raw_data: list) -> pd.DataFrame:
    """performs the common cleaning opperations"""
    # Parse the JSON response as a pd.DataFrame
    all_data_df = parse_challenge_response(raw_data)
    # Cleanup dataframe
    player_data_ranked = duckdb.query(
        """
        SELECT 
            "game.player.nick" AS player_nickname,
            "game.player.id" AS player_id, 
            ("game.player.totalScore.amount"::integer) AS total_score, 
            "game.map" AS game_map, 
            "game.token" AS game_token, 
            "game.player.totalDistance.meters.amount"::numeric AS total_distance,
            row_number() OVER (ORDER BY total_score DESC, total_distance ASC) AS challenge_rank,
            greatest(11 - challenge_rank, 0) as challenge_points
        FROM all_data_df
        ORDER BY total_score DESC, total_distance ASC
        """).to_df()

    return player_data_ranked

def process_final_results(
    df: pd.DataFrame, 
) -> pd.DataFrame:
    final_results = duckdb.query(
        """
        WITH base AS (
        SELECT 
            player_nickname,
            SUM(challenge_points)::integer AS total_points,
            row_number() OVER (ORDER BY total_points DESC) AS position,
            SUM(total_score)::integer AS sum_scores, 
            -- game_map, 
            -- game_token, 
            -- total_distance,
            -- challenge_rank,
            COUNT(*) AS challenges_played,
            player_id, 
        FROM df
        GROUP BY player_nickname, player_id
        ORDER BY total_points DESC, sum_scores DESC
        )
        SELECT
            position,
            player_nickname,
            total_points,
            sum_scores, 
            challenges_played,
            player_id,
        FROM base
        """).to_df()

    return final_results