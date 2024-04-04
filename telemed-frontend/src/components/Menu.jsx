
import React, {useState} from 'react';
import { Link } from 'react-router-dom';
import * as FaIcons from "react-icons/fa";
import * as AiIcons from "react-icons/ai";
import { IconContext } from "react-icons";
 

function Menu() {
  const [menuBar, setMenuBar] = useState(false);

  const showMenuBar = () => setMenuBar(!menuBar)
      


  const navStyle = {
    background: '#fff',
    height: '100vh',
    width: '250px',
    position: 'fixed',
    top: 0,
    left: '-100%',
    display: 'flex',
    justify: 'center',
    transition: '850ms',
  }

  const active = {
    
    transition: '500ms',
    background: '#fff',
    height: '100vh',
    width: '250px',
    position: 'fixed',
    top: 0,
    left: 0,
    display: 'flex',
    justify: 'center',
    
  }

  
  // className='bg-white h-[100vh] w-[250px] fixed left-[-100%] translate-x-10'

  return (
    <>
      <IconContext.Provider value={{color: undefined}}>
        <div className='flex  bg-white h-12 py-2.5 justify-start pl-5'>
          <Link to='#' className='bg-none text-3xl font-normal text-gray-700'>
            <FaIcons.FaBars  onClick={showMenuBar}/>
          </Link>
        </div>
          <nav style={menuBar ? (navStyle, active) : navStyle}  >
            <ul className='w-100' onClick={showMenuBar}>
              <li className='bg-white w-100 h-12 py-2.5 flex justify-start pl-5'>
                <Link to="#" className="bg-none text-3xl font-normal text-gray-700">
                    <AiIcons.AiOutlineClose />
                </Link>
              </li>

              <li className='text-gray-700 px-8 text-xl font-medium pb-2 pt-4'><Link to='/'>Home</Link></li>
            <li className='text-gray-700 px-8 text-xl font-medium py-2'><Link to='/About'>About</Link></li>
            <li className='text-gray-700 px-8 text-xl font-medium py-2'><Link to='/Services'>Services</Link></li>
            <li className='text-gray-700 px-8 text-xl font-medium py-2'><Link to='/Signup'>Register</Link></li>
            <li className='text-gray-700 px-8 text-xl font-medium py-2'><Link to='/Signin'>Login</Link> </li>     
            </ul>
                 
            
        </nav>
      </IconContext.Provider>
    </>
    
  )
}

export default Menu