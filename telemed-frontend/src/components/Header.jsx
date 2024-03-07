import React from 'react';
import heroImage from '../assets/heroimage.jpeg';



function Header() {
  return (
    <div className='w-full h-screen bg-no-repeat bg-cover' style={{ backgroundImage: `url(${heroImage})` }}>
       
       <div class="w-full h-full flex  justify-center items-center bg-black opacity-75">

       </div>

    </div>
  )
}

export default Header