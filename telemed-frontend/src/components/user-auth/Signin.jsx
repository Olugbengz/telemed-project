import { useState } from "react";
import React from 'react';

function signin() {
  const [loginData, setLoginData] = useState({
    email: '',
    password: ''
  })

  const handleSubmit = (event) => {
    const [name, value] = event.target
        setLoginData(prevloginData => {
          return {
            ...prevloginData,
            [name]: value
          }
        }
      )
  }

  const handleChange = () => {

  }
  return (
    <div>
     
      <form className='relative top-40 m-auto w-1/4 px-4 py-8 bg-white rounded-lg'>
      <h4 className='text-center font-medium my-6 text-2xl text-gray-600'>Log In</h4>
        <input
          className='bg-gray-200 appearance-none border-2 mb-3 border-gray-200 
          rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none
           focus:bg-white focus:border-purple-500' 
          type='Text'
          placeholder='Email'
          value={loginData.email}
          name="email"
          onChange={handleChange}        
        />

        <input 
          className='bg-gray-200 appearance-none border-2 mb-3 border-gray-200 
          rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none
           focus:bg-white focus:border-purple-500'
          type='Text'
          placeholder='Password'
          value={loginData.password}
          name="password"
          onChange={handleChange}        
        />
        <button
          className=' px-3 py-2 bg-purple-800 text-white rounded-lg mx-28 my-3.5 text-sm font-normal ' 
          type="submit" 
          onSubmit={handleSubmit}>
          Login
        </button>
      </form>
    </div>
  )
}

export default signin