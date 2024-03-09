import React, {useState} from 'react'

function Signup() {
    const [formData, setFormData] = useState({
        email: "",
        first_name: "",
        last_name: "",
        phone: ""
    })

function handleChange(event) {
    const {name, value, type} = event.target
    setFormData(prevFormData => {
       return {
        ...prevFormData,
        [name]: value
       } 
    })
}

function handleSubmit(event) {
    event.preventDefault()
    // submitToApi()
}

  return (
    <form className='relative top-40 m-auto w-1/4 px-4 py-8 bg-white rounded-lg' >
        <h4 className='text-center font-medium my-6 text-2xl text-gray-600'>Register</h4>
        <input
            className='bg-gray-200 appearance-none border-2 mb-3 border-gray-200 
            rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none
             focus:bg-white focus:border-purple-500'
            type='text'
            placeholder='First Name'
            name='first_name'
            onChange={handleChange}
            value={formData.first_name}
        />
        <input
            className='bg-gray-200 appearance-none border-2 mb-3 border-gray-200 
            rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none
             focus:bg-white focus:border-purple-500'
            type='text'
            placeholder='Last Name'
            name='last_name'
            onChange={handleChange}
            value={formData.last_name}
        />
        <input
            className='bg-gray-200 appearance-none border-2 mb-3 border-gray-200 
            rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none
             focus:bg-white focus:border-purple-500'
            type='text'
            placeholder='Email'
            name='email'
            onChange={handleChange}
            value={formData.email}
        />
        <input
            className='bg-gray-200 appearance-none border-2 mb-3 border-gray-200 
            rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none
             focus:bg-white focus:border-purple-500'
            type='text'
            placeholder='Mobile Phone'
            name='phone'
            onChange={handleChange}
            value={formData.phone}
        />
        <button className=' px-3 py-2 bg-purple-800 text-white rounded-lg mx-28 my-3.5 text-sm font-normal ' onSubmit={handleSubmit}>Submit</button>
    </form>
  )
}

export default Signup;