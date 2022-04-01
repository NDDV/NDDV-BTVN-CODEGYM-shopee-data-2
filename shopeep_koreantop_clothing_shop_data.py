#%%
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("shopeep_koreantop_clothing_shop_data.csv")
df.info()

# %%
df= df.dropna()
df.info()

# %%
df

# %%
#Vẽ biểu đồ:
#So sánh số lượng shop gia nhập theo các năm.
#Xu hướng của số lượng shop gia nhập theo từng tháng trong từng năm.
d1 = df.groupby(by=df['join_year']).count()

x = d1.index.get_level_values(0)
plt.plot(x , d1['pk_shop'],color='black',linestyle='--',marker='*')
plt.xlabel('year')
plt.ylabel('count')
plt.show()
# %%
d2 = df[['join_month', 'join_year','pk_shop']]
d2 = d2.groupby(['join_year','join_month']).count()
d2 = d2.sort_values(by=['join_year', 'join_month'])
d2
# %%
y = d2.index.get_level_values(0)
plt.bar(y , d2['pk_shop'],color='red')

for x1,y1 in zip(y, d2['pk_shop']):
    
    label = "{:.2f}".format(y1)

    plt.annotate(label,
                 (x1,y1),
                 textcoords="offset points",
                 xytext=(0,10),
                 ha='center')
    
plt.plot(x , d1['pk_shop'],color='black',linestyle='--',marker='*')
plt.xlabel('year')
plt.ylabel('count')
plt.show()

# %%
#Vẽ biểu đồ thể hiện mối quan hệ giữa 
#Tỉ lệ phản hồi với số lượt khách hàng đánh giá tốt
#Thời gian phản hồi (đơn vị giây) với số lượt khách hàng đánh giá tốt.
d3 = df[['response_rate','rating_good']]
d3 = d3.groupby(['response_rate']).count()
d3
#%%
z = d3.index.get_level_values(0)
plt.bar(z , d3['rating_good'],color='red')
plt.xlabel('response rate')
plt.ylabel('rating good')
plt.show()

# %%
d4 = df[['response_time','rating_good']]
d4['Second']=pd.to_datetime(d4['response_time'],format=' %H:%M:%S').dt.second
d4 = d4.groupby(['Second']).count()
d4

# %%
w = d4.index.get_level_values(0)
plt.bar(w , d4['rating_good'],color='red')
plt.plot(z , d3['rating_good'],color='black',linestyle='--',marker='o',markerfacecolor='blue',markersize='10')
plt.xlabel('Second till 60- Response rate till 100')
plt.ylabel('rating good')
plt.show()

# %%
