import React, {Suspense,lazy} from 'react';
import '../pages/home/style.scss';
import Loading from "../components/common/loading"

const HomeComponent = lazy(() => import("../pages/home/"));
const Home = (props) => {
  return (
    <Suspense fallback={<Loading />} >
      <HomeComponent {...props}></HomeComponent>
    </Suspense>
  )
};

const OauthComponent = lazy(() => import("../pages/oauth/"));
const Oauth = (props) => {
  return (
    <Suspense fallback={<Loading />}>
      <OauthComponent {...props}></OauthComponent>
    </Suspense>
  )
};


const TopicComponent = lazy(() => import("../pages/topic"));
const Topic = (props) => {
  return (
    <Suspense fallback={<Loading />}>
      <TopicComponent {...props}></TopicComponent>
    </Suspense>
  )
};
const NodeComponent = lazy(() => import("../pages/node"));
const Node = (props) => {
  return (
    <Suspense fallback={<Loading />}>
      <NodeComponent {...props}></NodeComponent>
    </Suspense>
  )
};

const SearchComponent = lazy(() => import("../pages/search"));
const Search = (props) => {
  return (
    <Suspense fallback={<Loading />}>
      <SearchComponent {...props}></SearchComponent>
    </Suspense>
  )
};

const NotFoundComponent = lazy(() => import("../pages/not-found"));
const NotFound = (props) => {
  return (
    <Suspense fallback={<Loading />}>
      <NotFoundComponent {...props}></NotFoundComponent>
    </Suspense>
  )
};

const AdminNodeComponent = lazy(() => import("../pages/admin-node"));
const AdminNode = (props) => {
  return (
    <Suspense fallback={<Loading />}>
      <AdminNodeComponent {...props}></AdminNodeComponent>
    </Suspense>
  )
};

const AdminSpiderComponent = lazy(() => import("../pages/admin-spider"));
const AdminSpider = (props) => {
  return (
    <Suspense fallback={<Loading />}>
      <AdminSpiderComponent {...props}></AdminSpiderComponent>
    </Suspense>
  )
};

const NoticeComponent = lazy(() => import("../pages/notice"));
const Notice = (props) => {
  return (
    <Suspense fallback={<Loading />}>
      <NoticeComponent {...props}></NoticeComponent>
    </Suspense>
  )
};


export default [

  {
    path:"/oauth",
    component: Oauth,
  },
  {
    path:"/topic/:id",
    component:Topic,
  },
  {
    path:"/node/:id",
    component:Node,
  },
  {
    path:"/search",
    component:Search,
    exact:true
  },
  {
    path: "/admin/node",
    exact: true,
    component: AdminNode,
  },
  {
    path: "/admin/spider",
    exact: true,
    component: AdminSpider,
  },
  {
    path: "/notice",
    exact: true,
    component: Notice,
  },

  {
    path: "/",
    exact: true,
    component: Home,
  },

  {
    path:"*",
    component: NotFound
  }
]