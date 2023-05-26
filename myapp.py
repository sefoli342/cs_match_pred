import pandas as pd
import streamlit as st


import streamlit as st
import joblib

import streamlit as st
from PIL import Image



model=joblib.load("model.pkl")

maps=["de_cache","de_dust2","de_inferno","de_mirage","de_nuke","de_overpass","de_train","de_vertigo"]
map_seçim1=st.sidebar.selectbox("Map seçiniz",maps)
map_seçim="de_cache"

kalan_süre=st.sidebar.number_input("Kalan süreyi giriniz",max_value=175.0,min_value=0.0,value=41.5)

bomba=st.sidebar.selectbox("Bomba Kuruldu mu?",[True,False])

kit=st.sidebar.number_input("CT Takımı defuse kit sayısı giriniz",step=1,min_value=0,max_value=5)

Counter_T_score=st.sidebar.number_input("Counter-Terorrist takımının skorunu giriniz",max_value=15,min_value=0,value=5)
T_score=st.sidebar.number_input("Terorrist takımının skorunu giriniz",max_value=15,min_value=0,value=5)

Ct_health=st.sidebar.number_input("CT-takımı sağlık toplamını yazınız",max_value=500,min_value=0,value=150)
t_health=st.sidebar.number_input("T-takımı sağlık toplamını yazınız",max_value=500,min_value=0,value=150)



import streamlit as st
from PIL import Image
col3, col4 = st.columns(2)
image1 =Image.open("csgo-esportimes.jpg")
image2=Image.open("logo-dark.png")
col3.image(image1)
col4.image(image2)




col1, col2 = st.columns(2)

ct_armor=col1.number_input("CT-takımının toplam armorunu yazınız",min_value=0,max_value=500,value=300)
t_armor=col2.number_input("T-takımının toplam armorunu yazınız",min_value=0,max_value=500,value=300)


col5, col6 = st.columns(2)

ct_money=col5.number_input("CT-takımının toplam parasını yazınız",min_value=0,max_value=80000,value=3000,step=50)
t_money=col6.number_input("T-takımının toplam parasını yazınız",min_value=0,max_value=80000,value=3000,step=50)

col7, col8 = st.columns(2)

ct_helmet=col7.number_input("CT-takımının toplam helmet sayısını yazınız",min_value=0,max_value=5,value=2,step=1)
t_helmet=col8.number_input("T-takımının toplam helmet sayısını yazınız",min_value=0,max_value=5,value=2,step=1)

col9, col10 = st.columns(2)
ct_alive=col9.number_input("CT-takımının hayattaki oyuncu sayısı toplamını yazınız",min_value=0,max_value=5,value=2,step=1)
t_alive=col10.number_input("T-takımının hayattaki oyuncu sayısı toplamını yazınız",min_value=0,max_value=5,value=2,step=1)


col11, col12 = st.columns(2)
ct_ak47=col11.number_input("CT-takımının AK-47 silahları  toplamını yazınız",min_value=0,max_value=5,value=2,step=1)
t_ak47=col12.number_input("T-takımının AK-47 silahlarının toplamını yazınız",min_value=0,max_value=5,value=2,step=1)


df=pd.read_excel(r"new_df.xlsx")

first_sample_list=[kalan_süre,Counter_T_score,T_score,map_seçim,bomba,Ct_health,t_health,ct_armor,t_armor,
                   ct_money,t_money,ct_helmet,t_helmet,kit,ct_alive,t_alive,ct_ak47,t_ak47]


sample_list=list(df.iloc[20,18:].values)

first_sample_list=first_sample_list+sample_list


df.loc[15194]=first_sample_list



df["AVG_REAL_HEALTH_T"]=(df["t_health"]*1.344 + df["t_armor"]*0.2)/df["t_players_alive"]
df["AVG_REAL_HEALTH_CT"]=(df["ct_health"]*1.344 + df["ct_armor"]*0.2)/df["ct_players_alive"]

df=df.fillna(0)

df["SAFE_LEVEL_T"]=pd.cut(df["AVG_REAL_HEALTH_T"],[-1,51.33,102.66,154.4],labels=["Low Level","Intermediate Level","High Level"])
df["SAFE_LEVEL_CT"]=pd.cut(df["AVG_REAL_HEALTH_CT"],[-1,51.33,102.66,154.4],labels=["Low Level","Intermediate Level","High Level"])



df.loc[((df["ct_weapon_ssg08"]+df["ct_weapon_awp"])>=1),"CT_LONG_RANGE"]="YES"
df.loc[((df["ct_weapon_ssg08"]+df["ct_weapon_awp"])<1),"CT_LONG_RANGE"]="NO"

df.loc[((df["t_weapon_ssg08"]+df["t_weapon_awp"])>=1),"T_LONG_RANGE"]="YES"
df.loc[((df["t_weapon_ssg08"]+df["t_weapon_awp"])<1),"T_LONG_RANGE"]="NO"



df.loc[((df["ct_weapon_cz75auto"]+df["ct_weapon_glock"]+df["ct_weapon_r8revolver"]+df["ct_weapon_deagle"]+df["ct_weapon_fiveseven"]+df["ct_weapon_usps"]+df["ct_weapon_p250"]+df["ct_weapon_p2000"]+df["ct_weapon_tec9"])>=4),"CT_IS_ECO"]="YES"
df.loc[((df["ct_weapon_cz75auto"]+df["ct_weapon_glock"]+df["ct_weapon_r8revolver"]+df["ct_weapon_deagle"]+df["ct_weapon_fiveseven"]+df["ct_weapon_usps"]+df["ct_weapon_p250"]+df["ct_weapon_p2000"]+df["ct_weapon_tec9"])<4),"CT_IS_ECO"]="NO"


df.loc[((df["t_weapon_cz75auto"]+df["t_weapon_glock"]+df["t_weapon_r8revolver"]+df["t_weapon_deagle"]+df["t_weapon_fiveseven"]+df["t_weapon_usps"]+df["t_weapon_p2000"]+df["t_weapon_tec9"])>=4),"T_IS_ECO"]="YES"
df.loc[((df["t_weapon_cz75auto"]+df["t_weapon_glock"]+df["t_weapon_r8revolver"]+df["t_weapon_deagle"]+df["t_weapon_fiveseven"]+df["t_weapon_usps"]+df["t_weapon_p2000"]+df["t_weapon_tec9"])<4),"T_IS_ECO"]="NO"




df.loc[(df["ct_score"]>df["t_score"]),"WHO_LEADS"]="CT"
df.loc[(df["t_score"]>df["ct_score"]),"WHO_LEADS"]="T"
df.loc[(df["t_score"]==df["ct_score"]),"WHO_LEADS"]="TIE"


df.loc[((df["ct_weapon_ak47"]+df["ct_weapon_m4a4"])>2),"Short_Damage_Power_CT"]="HIGH POWER"
df.loc[((df["t_weapon_ak47"]+df["t_weapon_m4a4"])>2),"Short_Damage_Power_T"]="HIGH POWER"


df.loc[((df["ct_weapon_m4a1s"]+df["ct_weapon_sg553"])>2),"Short_Damage_Power_CT"]="UPPER INTERMEDIATE POWER"
df.loc[((df["t_weapon_m4a1s"]+df["t_weapon_sg553"])>2),"Short_Damage_Power_T"]="UPPER INTERMEDIATE POWER"

df.loc[((df["ct_weapon_aug"]+df["ct_weapon_galilar"])>2),"Short_Damage_Power_CT"]="INTERMEDIATE POWER"
df.loc[((df["t_weapon_aug"]+df["t_weapon_galilar"])>2),"Short_Damage_Power_T"]="INTERMEDIATE POWER"


df.loc[((df["ct_weapon_aug"]+df["ct_weapon_galilar"]+df["ct_weapon_ak47"]+df["ct_weapon_m4a4"]+df["ct_weapon_m4a1s"]+df["ct_weapon_sg553"]+df["ct_weapon_aug"]+df["ct_weapon_galilar"])<=2),"Short_Damage_Power_CT"]="lOW POWER"
df.loc[((df["t_weapon_aug"]+df["t_weapon_galilar"]+df["t_weapon_ak47"]+df["t_weapon_m4a4"]+df["t_weapon_m4a1s"]+df["t_weapon_sg553"]+df["t_weapon_aug"]+df["t_weapon_galilar"])<=2),"Short_Damage_Power_T"]="LOW POWER"

def grab_col_names(dataframe, cat_th=15, car_th=20):
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
    num_but_cat = [col for col in dataframe.columns if
                   dataframe[col].nunique() < cat_th and dataframe[col].dtypes != "O"]
    cat_but_car = [col for col in dataframe.columns if
                   dataframe[col].nunique() > car_th and dataframe[col].dtypes == "O"]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    # num_cols
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]
    num_cols = [col for col in num_cols if col not in num_but_cat]

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')

    return cat_cols, num_cols, cat_but_car


cat_cols, num_cols, cat_but_car = grab_col_names(df)


dff=df.copy()

def one_hot_encoder(dataframe, categorical_cols, drop_first=False):
    dataframe = pd.get_dummies(dataframe, columns=categorical_cols, drop_first=drop_first)
    return dataframe
dff = one_hot_encoder(dff, cat_cols, drop_first=True)


from sklearn.preprocessing import MinMaxScaler

dff_s=MinMaxScaler().fit_transform(dff)


my_sample=dff_s[15193].reshape(1,-1)

surv = st.checkbox("Prediction ")
if surv:
    if model.predict(my_sample) == 1:
        st.success("Terorrist Win")
        image19 = Image.open("C:/Users/SEFA/OneDrive/Masaüstü/cs-go-101-620x350.jpg")
        st.image(image19)
    else:
        st.error("Counter-Terorrist Win")
        image20 = Image.open("C:/Users/SEFA/OneDrive/Masaüstü/csfoto.jpg")
        st.image(image20)





