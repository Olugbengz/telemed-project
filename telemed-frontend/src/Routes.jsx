import * as React from "react";
import { createBrowserRouter } from 'react-router-dom';
import Home from './components/Home';
// import ErrorPage from "./components/ErrorPage";



 export const router = createBrowserRouter([
    {
      path: "/",
      element: <Home />,
      // errorElement: <ErrorPage />,

    },
  ]);
