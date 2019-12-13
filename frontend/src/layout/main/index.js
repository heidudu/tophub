import React from 'react';
import './style.scss';
import {useSelector} from "react-redux";
import { getPcActive} from "../../redux/reducers/sidebar";



export default function (props) {
  const { children  }=props;
  const pcActivate = useSelector((state) => getPcActive(state));


  return(
    <div  styleName="box">
      <div styleName="box-top" > </div>
      <div className={`p-1  ${pcActivate?'active':null}`   }  styleName="box-content" id="box-content">{children}</div>
    </div>
  )
}

