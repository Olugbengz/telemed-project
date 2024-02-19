import { API } from '../../../backend';


export const getUsersDetails = () => {
    return fetch(`${API}users_account`, {method: 'GET'})
    .then((response) => response.json())
    .catch((err) => console.log(err))
};

// 