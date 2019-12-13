import React  from 'react'

import SignModal from './sign-modal'
import Head from './head'
import Toast from'./toast'


//style
import './style.scss'

export default function (props) {
  return (
    <div >
      <Head />
      <SignModal />
      <Toast />

    </div>
  )
}