import React,{useEffect} from 'react'
import Hero from '../components/Hero'
import Hero2 from '../components/Hero2'


export default function Home() {
    useEffect(()=>{
        window.scrollTo(0,0);
    })
  return (
    <div className='space-y-32'>
      <Hero/>
      <br />
      <br />
      <br />
      <br />
      <br />
      <Hero2/>
    </div>
  )
}
