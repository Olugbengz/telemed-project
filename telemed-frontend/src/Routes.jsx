import * as React from "react";
import { createBrowserRouter } from 'react-router-dom';
import Home from './components/Home';
import ErrorPage from "./components/ErrorPage";
import Signup from "./components/user-auth/signup";



 export const router = createBrowserRouter([
    {
      path: "/",
      element: <Home />,
      
      errorElement: <ErrorPage />,

    },
    {
      path: "signup/",
      element: <Signup />,
    },
  ]);
