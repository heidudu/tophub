import React from 'react';
import './style.scss';





export default function (props) {
  const { children  }=props;

  return(
    <div  styleName="box">
      <div styleName="box-top" > </div>
      <div className="  p-1 "  styleName="box-content" id="box-content">
        <div styleName="center-column">
          {children}
        </div>
        </div>
    </div>
  )

};