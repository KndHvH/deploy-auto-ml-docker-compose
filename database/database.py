

from sqlalchemy import text
from database.connection import get_connection
import pandas as pd
import datetime

CONNECTION = get_connection()

def save_predict(pred):
    cursor = CONNECTION.cursor()

    values = []
    for column in pred:
        values.append(pred[column].values[0])

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        f"""
        INSERT INTO weather_data (Wind_Direction, Wind_Speed, Humidity, Pressure, Power_Level, Light_Intensity, prediction_label, consult_date)
        VALUES ({values[0]},{values[1]},{values[2]},{values[3]},{values[4]},{values[5]},{values[6]},'{current_time}');
        """
    )

    CONNECTION.commit()
    cursor.close()


def create_table():

    cursor = CONNECTION.cursor()
    sql = '''
        CREATE TABLE IF NOT EXISTS weather_data (
            id SERIAL PRIMARY KEY,
            Wind_Direction INTEGER,
            Wind_Speed FLOAT,
            Humidity INTEGER,
            Pressure FLOAT,
            Power_Level FLOAT,
            Light_Intensity INTEGER,
            prediction_label INTEGER,
            consult_date DATE
        );
    '''
    cursor.execute(sql)
    CONNECTION.commit()
    cursor.close()


def get_predicts_in_db():
    cursor = CONNECTION.cursor()

    cursor.execute("SELECT * FROM weather_data;")
    results = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(results, columns=columns)

    cursor.close()

    return df