import React from 'react'
import { Switch, Route, BrowserRouter} from "react-router-dom";
import HomePage from './HomePage';

const App = () => {
    return (
        <BrowserRouter>
            <Switch>
                <Route path="/">
                    <HomePage></HomePage>
                </Route>
            </Switch>
        </BrowserRouter>
    )
}

export default App;