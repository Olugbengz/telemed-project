import React from 'react';
import { useRouteError } from 'react-router-dom';

function ErrorPage() {

    const error = useRouteError();
    console.error(error);

  return (
    <div>
        <h1>Oops!</h1>
        <p>Apologies, there are network glitches, data can't load now</p>
        <p>
            <i>{error.statusText || error.message}</i>
        </p>
    </div>
  )
}

export default ErrorPage