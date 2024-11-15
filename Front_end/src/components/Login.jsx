import React, { useState, useRef } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth0 } from "@auth0/auth0-react";
import {motion} from "framer-motion"
import "../../src/index.css"
// import Hero from "./Hero"; 

export const Login = () => {
  let form_inital = {
    email: "",
    password: "",
  };
  const [form, setform] = useState(form_inital);
  const [warning, setwarning] = useState(false);
  const { user, loginWithRedirect } = useAuth0();
  const history = useNavigate();
  const Email_ref = useRef();
  const password_ref = useRef();

  const handleFrom = (e) => {
    setform({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const handleGoogleauth = async (e) => {
    await loginWithRedirect();
    console.log(user);
    console.log("hello world");
    localStorage.setItem("token", user?.email);
    history("/");
  };

  const handleonSubmit = async (e) => {
    e.preventDefault();
    await fetch("http://localhost:3001/auth/Login", {
      method: "POST",
      body: JSON.stringify(form),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.error === "Please try to Login with correct credentials") {
          setwarning(true);

          setTimeout(() => {
            setwarning(false);
          }, 3000);
        } else if (data === "Internal Server Error") {
          console.log("in internal");
        } else {
          localStorage.setItem("token", data.authtoken);
          history("/");
        }
      })
      .catch((err) => {
        alert(err);
      });
  };

  return (
    <>
        <section 
        className="min-h-screen py-5 flex justify-center items-center w-full">
          <div className="container">
            <div className="row d-flex align-items-center justify-content-center">
              <div className="col-md-8 col-lg-7 col-xl-6">
                <motion.img
                initial={{x:-100}}
                animate={{x:0}}
                  src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/draw2.svg"
                  className="img-fluid"
                  alt="Phone image"
                />
              </div>
              <div className="col-md-7 col-lg-5 col-xl-5 offset-xl-1">
                <form method="post" onSubmit={handleonSubmit}>
                  <div className="form-outline mb-4">
                    <input
                      type="email"
                      name="email"
                      id="Email"
                      className="form-control form-control-lg"
                      onChange={handleFrom}
                      ref={Email_ref}
                      placeholder="johndoe@gmail.com"
                      required
                    />
                    <label className="form-label text-white" htmlFor="form1Example13">
                      Email address
                    </label>
                  </div>
                  <div className="form-outline mb-4">
                    <input
                      type="password"
                      id="Password"
                      name="password"
                      className="form-control form-control-lg"
                      onChange={handleFrom}
                      ref={password_ref}
                      placeholder="shhh!!! Enter password"
                      required
                    />
                    <label className="form-label text-white" htmlFor="form1Example23">
                      Password
                    </label>
                  </div>

                  <div className="d-flex justify-content-between align-items-center mb-4">
                    {/* Checkbox - input */}
                    <div className="form-check">
                      <input
                        className="form-check-input"
                        type="checkbox"
                        value=""
                        id="form1Example3"
                      />
                      <label className="form-check-label text-white" htmlFor="form1Example3">
                        {" "}
                        Remember me{" "}
                      </label>
                    </div>
                    <a href="#!">Forgot password?</a>
                  </div>

                  <button
                    type="submit"
                    className="btn btn-primary btn-lg btn-block"
                  >
                    Sign in
                  </button>

                  <div className="divider d-flex align-items-center my-4">
                    <p className="text-center fw-bold mx-3 mb-0 text-white">OR</p>
                  </div>
                  <div className="signbutton flex justify-center align-center gap-5">
                    <a
                      className="btn btn-Light btn-md btn-block Auth"
                      style={{ background: "white", border: "1.5px solid black" }}
                      href="#!"
                      role="button"
                      onClick={handleGoogleauth}
                    >
                      <i className="fab fa-twitter me-2">
                        {/* Google icon here */}
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
                        {/* Facebook icon here */}
                      </i>
                      Continue with Facebook
                    </a>
                  </div>
                </form>
                <br />
                <br />
                <h6
                  style={
                    warning
                      ? { display: "block", color: "red" }
                      : { display: "none" }
                  }
                >
                  Please try to Login with correct credentials
                </h6>
              </div>
            </div>
          </div>
        </section>

    </>
  );
};
