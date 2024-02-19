import {React, useState, useEffect} from 'react';
import { getUsersDetails } from './apicalls/docapicalls';


function Home() {

  const [users, setUsers] = useState([]);
  const [error, setError] = useState(false)

  const loadUsers = () => {
    getUsersDetails()
    .then((data) => {
      console.log(data)
      if (data.error) {
        setError(data.error)
        console.log(error)
      } else {
        setUsers(data)
      }
      
    });
  };

  useEffect(() => {
    loadUsers();
  }, [])

  return (
    <div>
    <h1>Hello world!</h1>

    
        {users.map((user, index) => {
            return (
              <ul className='flex flex-col gap-2' key={index}>
                  <l1 className='bg-white text-sm text-black font-normal '>{user.email}</l1>
              </ul>             
            
            )
          })  
        
        }
    
      
    </div>
  )
}

export default Home