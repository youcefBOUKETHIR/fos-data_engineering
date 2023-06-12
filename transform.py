import glob
import json
import pandas as pd


def get_all_filenames():
    filenames = glob.glob("raw_data_*.json")
    return filenames


filenames = get_all_filenames()

print(filenames)


def transform_one_file(filename):
    result = []

    with open(filename) as f:
        data = json.load(f)

    for city, city_data in data.items():
        latitude = city_data.get("latitude")
        longitude = city_data.get("longitude")
        temperature = city_data.get("current_weather").get("temperature")
        time = city_data.get("current_weather").get("time")

        city_dict = {
            "city": city,
            "latitude": latitude,
            "longitude": longitude,
            "temperature": temperature,
            "time": time,
        }

        result.append(city_dict)

    return result


def merge_all_files_in_pandas_df(files):
    output = []
    for fname in files:
        output_one_file = transform_one_file(fname)
        output.extend(output_one_file)
        df = pd.DataFrame(output)
    return df


def drop_duplicates(df_):
    df_.drop_duplicates(inplace=True)
    return df_


def main():
    files = get_all_filenames()
    df = merge_all_files_in_pandas_df(files)
    df = drop_duplicates(df)
    df.to_csv("transformed_data.csv", index=False)
if __name__=='__main__':
        main()