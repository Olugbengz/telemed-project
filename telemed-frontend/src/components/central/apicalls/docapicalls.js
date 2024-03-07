import { API } from '../../../backend';


export const getUsersDetails = () => {
    return fetch(`${API}doctors`, {method: 'GET'})
    .then((response) => response.json())
    .catch((err) => console.log(err))
};

// 