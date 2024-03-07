import {React, useState, useEffect} from 'react';
import { getUsersDetails } from '../components/central/apicalls/docapicalls';
import Header from './Header';
import DocCard from './DocCard';



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
    <div className='bg-slate-50'>
      <Header />
    <h1>Hello world!</h1>
    <div className='grid grid-cols-4'>
    {users.map((user, index) => {

      return (
        <div key={index} className='m-auto'>
          <DocCard 
            user={user}
           
          />
           
        </div>             

          )
        })  

      }
    </div>
    
        
    
      {/* <Footer /> */}
    </div>
  )
}

export default Home