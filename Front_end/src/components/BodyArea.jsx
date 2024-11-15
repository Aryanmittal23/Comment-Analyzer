import React, { useEffect } from "react";
import { Searchbar } from "./Searchbar";
import { Footer } from "./Footer";
import "../App.css";
import "./Footer.css";
import { useNavigate } from "react-router-dom";
import {motion} from 'framer-motion'
import bg from "../assets/bg.png"
// import { useAuth0 } from "@auth0/auth0-react";

export const BodyArea = () => {
  const history = useNavigate();
  // const { user, loginWithRedirect,isAuthenticated} = useAuth0();

  useEffect(() => {
    if (!localStorage.getItem("token")) {
      history("/Login");
    }
  },[]);
  return (
    <div className="flex flex-row min-h-screen gap-5">
      <motion.img 
      initial={{x:-100,opacity:0}}
      animate={{x:0,opacity:1}}
      transition={{type:'spring',duration:0.3}}
      className="w-[430px] ml-5 h-[530px] mt-20"
      src={bg}/>
      <div className="flex flex-col justify-center align-center items-center gap-8">
        <motion.div 
        initial={{x:-100,opacity:0}}
        animate={{x:0,opacity:1}}
        transition={{type:'tween'}}
        className="text-2xl text-gray-200 font-bold ">
          <h1>Please enter the Youtube Video Url to analyse comments.</h1>
        </motion.div>
        <div className="searchbar">
          <Searchbar></Searchbar>
        </div>
      </div>
    </div>
  );
};
