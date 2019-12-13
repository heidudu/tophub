import React from 'react';
import './style.scss';
import {Link} from "react-router-dom";
import dateStr from '../../vendors/parse-time';
import FollowButton from '../common/follow'



export default function(props) {

  const {data} = props;
  return (

    <div className="p-3">
      <div styleName="detail-nav" role="tablist" className="nav nav-tabs d-flex justify-content-around mb-4 text-center  text-dark ">
        <a href="#related-content" id="related-content-tab" data-toggle="pill" styleName="nav-item" className=" active" role="tab" aria-controls="related-content" aria-selected="true">相关内容</a>
        <a href="#related-node" id="related-node-tab" data-toggle="pill" styleName="nav-item" role="tab" aria-controls="related-node" aria-selected="false">相关节点</a>
      </div>
      <div  className=" card flex-fill tab-pane fade  show active" id="related-content" role="tabpanel" aria-labelledby="related-content-tab">
        <div className="card-body px-1 px-md-2 px-lg-3" >
          <span className="card-title mb-3 d-flex" >相关内容</span>
          <div className="card-text ">
            {data.content?
              data.content.map((item,index)=>{
              return(
                <a href={item.url} target="_blank" rel="noopener noreferrer" styleName="card-body-item" className="d-flex justify-content-between  mb-3 text-dark" key={index}>
                  <img styleName="related_img" alt="card-img" src={item.source_img}/>
                  <span className=" text-left col px-1 px-md-2 px-lg-3" >{item.title}</span>
                  {/*<span className="text-muted d-flex text-left " >{item.source_name}•{item.node_name}</span>*/}
                  <span className="text-muted d-flex  " style={{maxWidth:"34%",overflow:"hidden",whiteSpace:"nowrap"}}>{dateStr(item.time)}</span>
                </a>
              )
            })
            :
            null
            }
          </div>
        </div>
      </div>
      <div  className=" card flex-fill tab-pane fade" id="related-node" role="tabpanel" aria-labelledby="related-node-tab">
        <div className="card-body" >
          <span className="card-title mb-3 d-flex" >相关节点</span>
          <div className="card-text">
            {data.nodes?
              data.nodes.map((item,index)=>{
              return(
                <div  styleName="detail_related" className="d-flex justify-content-between  mb-3 text-dark" key={index}>
                  <Link to={`/node/${item.id}`} className="text-dark col-10 pl-0">
                    <img  styleName="related_img" alt="card-img" src={item.source_img}/><span >{item.source_name}{item.topic_name==="博客"?null:`•${item.name}`}</span>
                  </Link>
                  <FollowButton targetId={item.id}/>
                </div>
              )
            })
            :
            null
            }
          </div>
        </div>
      </div>

    </div>
  )
 }