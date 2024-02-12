// import { API } from '../../../backend';


export const getUsersDetails = () => {
    return fetch('http://127.0.0.1:8000/apis/users_account', {method: 'GET'})
    .then((response) => response.json())
    .catch((err) => console.log(err))
};