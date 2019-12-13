import React from 'react';


// config
import { api, } from '../../../config';


// components
import Modal from '../../../components/common/modal';


// styles
import './style.scss'

export default function(props) {

  const body = (<div styleName="layer">
          <div styleName="other-sign-in">
            <span>GITHUB方式登录</span>
          </div>
          <div styleName="social" className="row">
            <div className={`col-12`}>
              <a href={`${api.domain}/oauth/github`} styleName="github">GitHub</a>
            </div>
          </div>
        </div>);

  return (<div>
    <Modal
      id="sign"
      body={body}
      />
  </div>)

}