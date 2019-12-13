import React, { useState, useEffect } from 'react';
import MainColumn from '../../layout/main'
import parseUrl from "../../utils/parse-url";

let titleList = {
  'wrong_token': '无权访问',
  'error':`登录失败，请重试 <span  data-toggle="modal" data-target="#sign" >登陆</span>`,
  'create_user_failed': '创建用户失败',
  'create_token_failed': '创建token失败',
};



export default function (props) {
  const [ tips, setTips ] = useState('');
  const notice =  parseUrl(props.location.search)['notice'];

  useEffect(()=>{
    setTips(titleList[notice] || '未知提醒')
  }, []);




  return(
    <MainColumn>
      <div style={{ textAlign:'center' }}>
        <h3 dangerouslySetInnerHTML={{__html:tips}} />
      </div>
    </MainColumn>
  )
}