import React, {useState, useEffect} from 'react'
import { useParams } from 'react-router-dom'
import { API } from '../backend'

function DocDetails() {
const params = useParams()
const [doc, setDoc] = useState({})

console.log(`${API}doctors/${params.id}`)
useEffect(() => {
    fetch(`${API}doctors/${params.id}`)

    .then(resp => (resp.json()))
    .then(data => setDoc(data)) 
}, [params.id])




  return (
    <div className='mx-10 my-16'>
        <h4 className='text-3xl text-white'>Doctor's details</h4>
      <br/>
      <ul className='m-auto'>
        <li className='text-xl text-white'>Doctor: Dr. {doc.doctor}</li>
        <li className='text-xl text-white'>Specialty: {doc.specialty}</li>
        <li className='text-xl text-white'>Years of Experience: {doc.years_of_experience}</li>
        <li className='text-xl text-white'>Location: {doc.location}</li>
      </ul>

    </div>
  )
}

export default DocDetails