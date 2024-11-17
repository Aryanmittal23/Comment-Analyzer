import React, { useState } from "react";
import { FcGoogle } from "react-icons/fc";
import { ImFacebook2 } from "react-icons/im";
import { useNavigate } from "react-router-dom";
// import { useAuth0 } from "@auth0/auth0-react";
import "../index.css"
import {motion} from 'framer-motion'

function App() {
  const history = useNavigate();
  const form1 = {
    username: "",
    email: "",
    password: "",
  };
  const [form, setform] = useState(form1);
  const [warning, setwarning] = useState(false);
  // const { user,loginWithRedirect } = useAuth0();

  //handlers
  const handleSignup = async (e) => {
    e.preventDefault();
    await fetch("http://localhost:3001/auth/signup/", {
      method: "POST",
      body: JSON.stringify(form),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        if (data.authtoken) {
          localStorage.setItem("token", data.authtoken);
          history("/");
        } else if (data.data == "exists") {
          setwarning(true);
          setform(form1);
          setTimeout(() => {
            setwarning(false);
          }, 3000);
        } else if (data === "Internal Server Error") {
          console.log("in internal");
        }
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const handleChange = (e) => {
    setform({ ...form, [e.target.name]: e.target.value });
  };

  return (
    <div className="container-fluid p-4">
      <div className="row">
        <div className="col-md-6 d-flex flex-column justify-content-center text-center text-md-start">
          <motion.h1 
          initial={{x:-100,opacity:0}}
          animate={{x:0,opacity:1}}
          exit={{x:100,opacity:0}}
          transition={{type:'spring',damping:10,stiffness:200,duration:0.8}}
          className="my-5 display-3 fw-bold ls-tight px-3 heading text-white">
            Decode Comments <br />
            <motion.span className="text-primary">Elevate Insights.</motion.span>
          </motion.h1>
          <motion.p 
          initial={{y:-100,opacity:0}}
          animate={{y:0,opacity:1}}
          transition={{type:'tween',duration:0.3,delay:0.1}}
          className="px-3" style={{ color: "hsl(217, 10%, 50.8%)" }}>
            Sentiment analysis, a powerful application of machine learning,
            involves the automatic identification and classification of emotions
            conveyed within a piece of text. By leveraging natural language
            processing algorithms, sentiment analysis enables machines to
            discern whether a text expresses positive, negative, or neutral
            sentiments.
          </motion.p>
        </div>

        <div className="col-md-6 ">
          <motion.div 
          initial={{y:-100,opacity:1}}
          animate={{y:0,opacity:1}}
          transition={{type:'tween',duration:0.2,damping:150,stiffness:500}}
          className=" my-5 bg-black">
            <div className=" p-5 bg-black">
              <form onSubmit={handleSignup}>
                <input
                  className="form-control w-full mb-4"
                  type="text"
                  name="username"
                  minLength={3}
                  placeholder="Username"
                  value={form.username}
                  onChange={handleChange}
                  required
                />
                <input
                  className="form-control mb-4"
                  type="email"
                  name="email"
                  placeholder="Email"
                  value={form.email}
                  onChange={handleChange}
                  required
                />
                <input
                  className="form-control mb-4"
                  type="password"
                  name="password"
                  placeholder="Password"
                  value={form.password}
                  minLength={5}
                  onChange={handleChange}
                  required
                />

                <div className="d-flex justify-content-center mb-4">
                  <div className=" bg-black">
                    <input
                      className="form-check-input"
                      type="checkbox"
                      name="condition-box"
                      value=""
                      id="flexCheckDefault"
                      required
                    />
                    <label
                      className=" text-white bg-black"
                      htmlFor="flexCheckDefault"
                    >
                      Terms and Conditions
                    </label>
                  </div>
                </div>

                <button className="btn btn-primary w-100 mb-4 text-white" type="submit">
                  Sign up
                </button>
                <h6
                  style={
                    warning
                      ? { display: "block", color: "red" }
                      : { display: "none" }
                  }
                >
                  User Already Exists Please Login
                </h6>
              </form>

              <div className="divider d-flex align-items-center my-4">
                <p className="text-center fw-bold mx-3 mb-0 text-white bg-black flex justify-center align-center items-center">OR</p>
              </div>

              <div className="signbutton flex gap-4 items-center justify-center bg-black">
                <a
                  className="btn btn-light btn-md btn-block Auth"
                  style={{ background: "white", border: "1.5px solid black" }}
                  href="#!"
                  role="button"

                >
                  <i className="fab fa-twitter me-2">
                    <FcGoogle />
                  </i>
                  Continue with Google
                </a>

                <a
                  className="btn btn-primary btn-md btn-block"
                  style={{ background: "#3b5998" }}
                  href="#!"
                  role="button"
                >
                  <i className="fab fa-facebook-f me-2">
                    <ImFacebook2 />
                  </i>
                  Continue with Facebook
                </a>
              </div>
            </div>
          </motion.div>
        </div>
      </div>
    </div>
  );
}

export default App;
