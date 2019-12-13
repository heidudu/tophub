import React, {Suspense, lazy, useEffect}from 'react';
import {Provider} from 'react-redux'
import { BrowserRouter } from 'react-router-dom';
import store from './redux'
import routes from './router'
import './theme/global.scss'
import {loadUserInfo} from "./redux/actions/user";
import {renderRoutes}  from 'react-router-config'




const GlobalComponent = lazy(() => import("./components/global/"));
const Global = (props) => {
  return (
    <Suspense fallback={null}>
      <GlobalComponent {...props}></GlobalComponent>
    </Suspense>
  )
};



function App(props) {
  useEffect(()=>{
    loadUserInfo()(store.dispatch, store.getState)
    }
  );



  return (
    <Provider store={store}>
      <BrowserRouter >
        <Global {...props}/>
        {/*<div className="container "  >*/}
        {renderRoutes(routes)}
        {/*</div>*/}
      </BrowserRouter>
    </Provider>
  );
}



export default App;
