import React from 'react'
import Plx from "react-plx"
import {motion} from "framer-motion"
import { Login } from './Login';
import "../../src/index.css"

const divParallaxData = [
    {
      start: 0,
      end: 500,
      properties: [
        {
          startValue: 1,
          endValue: 2,
          property: "scale",
        },
      ],
    },
];

const paragraphParallaxData = [
    {
      start: 0,
      end: 500,
      properties: [
        {
          startValue: 1,
          endValue: 0,
          property: "opacity",
        },
      ],
    },
  ];
  
export default function Hero() {
  return (
    <>
    <Plx parallaxData={divParallaxData}>
        <div className='text-gray-500 mt-10 md:flex justify-center items-center p-4 flex-col'>
          <div className="md:w-1/2 w-full flex justify-center items-center flex-col text-center">
            <motion.h1
              initial={{ x: -500, opacity: 0 }}
              animate={{ x: 0, opacity: 1 }}
              transition={{ duration: 0.5, delay: 0.1 }}
              className="font-semibold md:text-[60px] text-center md:text-start"
            >
              <span className="font-bold block md:inline-block !text-blue-500 text-[80px] mr-4">
                Comment Analyser
              </span>
              <br />
              <span className='font-semibold '>From Text to Insight: Analyzing Comments for a </span><span className='font-semibold text-blue-500'>Better Web.</span>
            </motion.h1>
            <motion.div
          initial={{ x: -500, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          transition={{ duration: 0.5, delay: 0.2 }}
        >
          <Plx parallaxData={paragraphParallaxData} className="my-4 text-center md:text-start">
          Explore the impact of words in shaping online spaces{" "}
            <a href='https://comment-analyzer-doc.streamlit.app/' className="text-blue-500 underline cursor-pointer">
              Learn More
            </a>
          </Plx>
        </motion.div>
        <motion.div
          initial={{ x: -500, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          transition={{ duration: 0.5, delay: 0.3 }}
          className="w-full flex md:block"
        >
          <a href="#hero2"
            type="button"
            className="my-4 py-3 px-6 md:px-4 gap-x-2 mx-auto md:w-1/5 text-md font-semibold rounded-3xl text-center border border-transparent bg-blue-600/80 text-white hover:bg-blue-700/50 disabled:opacity-50 disabled:pointer-events-none dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600"
          >
            Get Started
          </a>
        </motion.div>
          </div>
        </div>
    </Plx>

    </>
  )
}
