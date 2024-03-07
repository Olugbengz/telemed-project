import React from 'react'

function DocCard(props) {
  // const { doctors } = props;
  // if (!doctors || doctors.length === 0) return <p>Sorry, no doctor is available now!</p>
  return (
    <div  className='w-[300px]  flex flex-col gap-3 border-2 border-gray-300 shadow-md items-start justify-center rounded-lg'>
          <img 
              className='w-full max-h-[160px] rounded-tl-lg rounded-tr-lg' 
              key={props.profile_image}
              src={props.profile_image || null}
          />

          <h3 
            className='font-sans text-xl text-gray-900 font-bold p-2'>            
              {props.user.doctor ? (
                <>
                   Dr. {props.user.doctor}
                </>
              )  : (
                <p>Your doctor is not on this platform</p>
              )
            }
               

          </h3>    

          <p className='font-san text-sm text-gray-600 font-normal p-2'>
            A <span className='italic font-light'>{props.user.specialty || null}</span>,
            with <span>{props.user.years_of_experience || null}</span> years experience
        </p>
      

        <div className=' flex items-center gap-8 justify-start ml-2 my-2'>
            
            <div className='flex gap-2'>{props.user.language || null}</div>
                
                {/* <a href={props.link} target='_blank' className='bg-green-900 inline-block italic antialiased font-light text-white text-lg cursor-pointer px-3.5 py-1.5 w-12 rounded-full'><IoGitBranch /></a> */}
        </div>
        

    </div>
  )
}

export default DocCard