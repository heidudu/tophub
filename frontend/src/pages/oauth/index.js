import React, {useEffect} from 'react';
import parseUrl from '../../utils/parse-url'
import {_signInRequest} from "../../api";
import Toastify from "toastify-js";
import Loading from "../../components/common/loading"

function Oauth(props) {

  useEffect(()=>{
    const access_token =  parseUrl(props.location.search)['access_token'];
    if(access_token) {
      _signInRequest(access_token).then(([err,res]) => {
        if(err){
          Toastify({
            text: "登录失败.请重试",
            duration: 3000,
            backgroundColor: 'linear-gradient(to right, #0988fe, #1c75fb)'
          }).showToast();
        window.location.href = '/';

        }else if (res && res.success){
          window.location.href = '/';
        }
      })
    }else{
      Toastify({
        text: "登录失败.请重试",
        duration: 3000,
        backgroundColor: 'linear-gradient(to right, #0988fe, #1c75fb)'
      }).showToast();
      window.location.href = '/';
    }
  });
  return(
    <Loading />
  );
}



export default Oauth