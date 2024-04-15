
import { API } from '../../../backend';


export const getUsersDetails = () => {
    return fetch(`${API}doctors`, {method: 'GET'})
    .then((response) => response.json())
    .catch((err) => console.log(err))
};


// export const getDocDetails = (id) => {
//     fetch(`${API}doctors/${id}`, {method: 'GET'})
//     .then(resp => resp.json())
//     .catch((err) => console.log(err))
// };