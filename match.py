import pandas as pd


input_data_file = r"E:\data\sgpnew/ccn-cn-240321/matched_data_ccn_light4.csv"
output_data_file = r"E:\data\sgpnew/ccn-cn-240321/matched_data_ccn_light3.csv"

df1 = pd.read_csv(input_data_file)
df2 = pd.read_csv(output_data_file)


df1['Date'] = pd.to_datetime(df1['Time']).dt.strftime('%Y-%m-%d %H:%M')  # 包括分钟部分
df2['Date'] = pd.to_datetime(df2['Time']).dt.strftime('%Y-%m-%d %H:%M')  # 包括分钟部分
    

df2 = df2[df2['Date'].isin(df1['Date'])]
df2.drop(columns=['Date'], inplace=True)
df1.drop(columns=['Date'], inplace=True)


matched_data = df2.copy()


matched_data['Time'] = pd.to_datetime(matched_data['Time'])
matched_data['Time'] = matched_data['Time'].dt.round('T')  # 'T' 表示分钟级别
matched_data = matched_data.drop_duplicates(subset=['Time'], keep='first')


output_matched_data_file = r"E:\data\sgpnew/ccn-cn-240321/matched_data_ccn_light5.csv"
matched_data.to_csv(output_matched_data_file, index=False)
print(f"Matched data has been saved to {output_matched_data_file}")
