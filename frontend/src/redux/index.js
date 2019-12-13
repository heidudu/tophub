import { createStore, applyMiddleware, combineReducers,compose} from 'redux';
import thunk from 'redux-thunk';
import rootReducer from './reducers';


let middleware = [ thunk ];

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
const store = createStore(
  combineReducers(rootReducer),
  composeEnhancers(applyMiddleware(...middleware))
);



export default store;