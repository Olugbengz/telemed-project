import * as React from "react";
import { createBrowserRouter } from 'react-router-dom';
import Home from './components/central/Home';



 export const router = createBrowserRouter([
    {
      path: "/",
      element: <Home />,
    },
  ]);
