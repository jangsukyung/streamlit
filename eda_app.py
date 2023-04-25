# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import utils

def run_eda_app():
    st.subheader("탐색적 자료 분석")

    iris = pd.read_csv('data/iris.csv')
    st.markdown('## IRIS 데이터 확인 -head()만 적용')
    st.write(iris) # print()

    # 메뉴 지정
    submenu = st.sidebar.selectbox('하위 메뉴', ['기술통계량', '그래프분석', '통계분석'])
    if submenu == '기술통계량':
        st.dataframe(iris)

        with st.expander('데이터 타입'):
            result1 = pd.DataFrame(iris.dtypes)
            st.write(result1)
        with st.expander('기술 통계량'):
            result2 = iris.describe()
            st.write(result1)

        with st.expander("타깃 빈도 수 확인"):
            st.write(iris['species'].value_counts())

    elif submenu == '그래프분석':
        st.title("Title")
        with st.expander('산점도'):
            fig1 = px.scatter(iris, x = 'sepal_width',
                             y = 'sepal_length',
                             color = 'species',
                             size = 'petal_width',
                             hover_data = ['petal_length'])
            st.plotly_chart(fig1)

        # layouts
        col1, col2 = st.columns(2)
        with col1:
            st.title('Seaborn')
            # 그래프 작성
            fig2, ax = plt.subplots()
            sns.scatterplot(data = iris,
                            x = 'sepal_width',
                            y = 'sepal_length')
            st.pyplot(fig2)

        with col2:
            st.title('Matplotlib')
            # 그래프 작성
            fig3, ax = plt.subplots()
            ax.scatter(x = 'sepal_width', y = 'sepal_length', data = iris)
            st.pyplot(fig3)

        # Tabs
        tab1, tab2 = st.tabs(['탭1', '탭2'])
        with tab1:
            st.write('탭1')
            # 종 선택할 때마다
            # 산점도 그래프가 달라지도록 함.
            # plotly 그래프로 구현
            choice = st.selectbox('종', iris['species'].unique())
            result = iris[iris['species'] == choice].reset_index(drop=True)

            fig4, ax = plt.subplots()
            fig4 = px.scatter(result, x = result['sepal_length'], y = result['sepal_width'])
            st.plotly_chart(fig4, use_container_width=True)

        with tab2:
            st.write('탭2')
            # 캐글 데이터 / 공모전 데이터
            # 해당 데이터 그래프 1개만 그려본다.
            consult = pd.read_csv('data/consulting.csv', encoding = 'cp949')
            st.line_chart(consult)


    elif submenu == '통계분석':
        pass
    else:
        st.warning("뭔가 없어요!")