import React, { useEffect, useRef, useState } from "react";
import { MdDarkMode } from "react-icons/md";
import { MdLightMode } from "react-icons/md";
import { Link } from "react-router-dom";
import "./Navbar.css"
import { useAuth0 } from "@auth0/auth0-react";
import {motion} from 'framer-motion'
import logo from "../assets/logo2.png"
import { useNavigate } from "react-router-dom";
import "../index.css"

export const Navbar = () => {
const navigate=useNavigate()
const [mode,setMode] =  useState("light");
const [login,setlogin] = useState("LoggedIn");
const { user, loginWithRedirect,isAuthenticated} = useAuth0();

useEffect(()=>
{
  if(localStorage.getItem("token"))
  {
    setlogin("LoggedOut");
  }
},[user]);
 const handleOnLogin = ()=>
{
  localStorage.removeItem("token");
  setlogin("LoggedIn");
} 
const handleHome=()=>{
  navigate('/');
}
const handleDocumentation=()=>{
  navigate('https://comment-analyzer-doc.streamlit.app/');
}
const handleInsight=()=>{
  navigate('/body');
}
 return (
    <>
      <header className=" text-white">
        <div className="flex justify-between px-8 py-4 items-center gap-16">
            <div className="ml-0 flex items-center gap-3 text-3xl font-bold">
            Comment Analyser
            </div>
            <nav className="">
              <ul className="flex gap-6 text-lg md:text-base">
                <li onClick={handleHome} className="text-lg p-4 border-b-2 dark:hover:text-indigo-200 dark:hover:border-indigo-200 border-indigo-500 border-opacity-0 hover:border-opacity-100 hover:text-indigo-500 duration-200 cursor-pointer active">Home</li>
                <li className="text-lg p-4 border-b-2 dark:hover:text-indigo-200 dark:hover:border-indigo-200 border-indigo-500 border-opacity-0 hover:border-opacity-100 hover:text-indigo-500 duration-200 cursor-pointer active">
                  <a href="https://comment-analyzer-doc.streamlit.app/"
                  target="_blank" 
                  className="no-underline text-white hover:text-indigo-500">
                  Documentation</a></li>
                <li 
                onClick={handleInsight}
                className="text-lg p-4 border-b-2 dark:hover:text-indigo-200 dark:hover:border-indigo-200 border-indigo-500 border-opacity-0 hover:border-opacity-100 hover:text-indigo-500 duration-200 cursor-pointer active">Get Insights</li>
              </ul>
              </nav>
            <div className="text-end button d-flex gap-2 ">
              <Link to="/Login"
              className="px-4 py-2 bg-gray-600 text-white btn-outline-dark me-2 Login hover:scale-110 hover:bg-gray-800 hover:text-black
              rounded-xl" 
              onClick={handleOnLogin}>{login === "LoggedOut" ? "Logout" : "Login"}</Link>
          </div>
        </div>
      </header>
    </>
  );
};
