import * as React from "react";
import { createBrowserRouter, Link, Outlet } from 'react-router-dom';
import Home from './components/Home';
import Services from './components/Services';
import About from './components/About';
import ErrorPage from "./components/ErrorPage";
import Signup from "./components/user-auth/Signup";
import Signin from "./components/user-auth/Signin";
import Menu from "./components/Menu";
import DocDetails from "./components/DocDetails";

function AppLayout() {
  return (
    <>
      <Menu />
      <Outlet />
    </>
  )
}

 export const router = createBrowserRouter([
    {
      element: <AppLayout />,
      children: [
        {
          path: "/",
          element: <Home />,
          
          errorElement: <ErrorPage />,
    
        },
        {
          path: "about/",
          element: <About />,
        },
        {
          path: "services/",
          element: <Services />,
        },
        {
          path: "signup/",
          element: <Signup />,
        },
        {
          path: "signin/",
          element: <Signin />,
        },
        {
          path: "/doc/:id",
          element: <DocDetails />,
        },
      ] 
    }
    
  ]);
