import axios from 'axios'
import {api} from "../config";



export default (url, method = 'get', data = {} ,take_cookie = false, input_headers = {}) => {
  let headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/json;charset=utf-8',
    'Access-Control-Allow-Origin': 'http://localhost:5000',
    'Access-Control-Allow-Credentials': 'true',
    'Access-Control-Allow-Headers':'Content-Type, X-Requested-With, Access-Control-Allow-Origin,Access-Control-Allow-Credentials',
    ...input_headers

  };
  let baseURL = api.domain;
  let option = { url, method, headers,baseURL };
  if (take_cookie === true){
    option.withCredentials = true;
  }


  if (method === 'get' ) {
    option.params = data
  } else if (method === 'post'|| method ==='delete'|| method ==='put') {
    option.data = data
  }

  return axios(option).then(resp => {
      if (resp && resp.data) {

        let res = resp.data;
        return [null, res]
      } else {
        return ['return none',null]
      }
    }).catch(function(error) {
      // console.log(Reflect.ownKeys(error));
      if (error.response && error.response.data) {
        return [error.response.data.message,null]
      }
      else if (error.message) {
        return [error.message,null]
      } else {
        return ['return error',null]
      }

    })
}
