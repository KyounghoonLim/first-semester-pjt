import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '@/views/Main';
import Detail from '@/components/movies/Detail';
import Signup from '@/components/accounts/Signup';
import Login from '@/components/accounts/Login';
import Community from '@/components/community/Community_Main';
import CommunityDetail from '@/components/community/Community_Detail';
import MovieChoice from '@/components/movies/MovieChoice';
//추가한 부분 
import Comment from '@/components/community/comment/Comment';
import CommunityCreate from '@/components/community/Community_Create';
import ProfileOther from '@/components/accounts/profile_other/ProfileOther';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Main',
    component: Main
  },
  {
    path: '/detail/:movieId',
    name: 'Detail',
    component: Detail,
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/community',
    name: 'Community',
    component: Community
  },
  {
    path: '/community/detail/:articleId',
    name: 'Community_Detail',
    component: CommunityDetail
  },
  {
    path: '/moviechoice',
    name: 'MovieChoice',
    component: MovieChoice
  },


  // 추가한 부분 
  {
    path: '/community/:articleId/comment',
    name: 'Comment',
    component: Comment 
  },
  {
    path: '/community/create',
    name: 'Community_Create',
    component: CommunityCreate
  },
 // 다른 사람 프로필 
  {
    path: '/profile/:username',
    name: 'ProfileOther',
    component: ProfileOther
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
import Profile from '@/components/accounts/profile/Profile';
router.beforeEach((to, from, next) => {
  if (Profile.user && Profile.user.like_genres.length == 0 && to.name !== 'MovieChoice') next({ name: 'MovieChoice' })
  else if ((to.name !== 'Login' && to.name !== 'Signup') && !localStorage.getItem('jwt')) next({ name: 'Login' })
  else if ((to.name == 'Login' || to.name == 'Signup') && localStorage.getItem('jwt')) next({ name: 'Main' })
  else next()
})

export default router
