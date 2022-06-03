import streamlit as st
import random
from   time import time

@st.experimental_memo
def generate_data(size):
    data = []
    for i in range(size):
        data.append(random.randint(1, 100))
    return data

def bubble_sort(data):
    with st.empty():
        for i in range(len(data)):
            for j in range(len(data) - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    st.bar_chart(data)

def selection_sort(data):
    with st.empty():
        for i in range(len(data)):
            min_index = i
            for j in range(i + 1, len(data)):
                if data[j] < data[min_index]:
                    min_index = j
            data[i], data[min_index] = data[min_index], data[i]
            st.bar_chart(data)

def insertion_sort(data):
    with st.empty():
        for i in range(1, len(data)):
            j = i
            while j > 0 and data[j] < data[j - 1]:
                data[j], data[j - 1] = data[j - 1], data[j]
                j -= 1
                st.bar_chart(data)

if __name__ == '__main__':
    st.set_page_config(page_title='Sorting Visualizer', page_icon='📊', layout='wide')
    st.title('Sorting Visualizer')
    cols = st.columns(2)
    data_size = cols[0].number_input('Data Size', min_value=10, max_value=1000, value=50)
    sort_algo = cols[1].selectbox('Sort Algorithm', ['Bubble Sort', 'Selection Sort', 'Insertion Sort']) 
    data = generate_data(int(data_size))
    if st.button('Start'):
        t_start = time()
        if sort_algo == 'Bubble Sort':
            bubble_sort(data)
        elif sort_algo == 'Selection Sort':
            selection_sort(data)
        elif sort_algo == 'Insertion Sort':
            insertion_sort(data)
        st.write('Time taken:', round(time() - t_start, 4), 'seconds')
    else:
        st.bar_chart(data)
