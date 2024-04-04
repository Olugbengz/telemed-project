import axios from 'axios';

const baseURL = 'http://127.0.0.1:8000/apis/'

const axiosInstance = axios.create({
    baseUrl: baseURL,
    timeout: 5000,
    headers: {
        Authorization: localStorage.getItem('access_token')
        ? 'JWT' + localStorage.getItem('access_token')
        : null,
        'Conten-Type': 'application/json',
        accept: 'application/json'
    },
});

export default axiosInstance;