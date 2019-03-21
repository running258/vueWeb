// module.exports = [{
//     name: '接口',
//     id: 'interface',
//     sub: [{
//       name: '工程目录',
//       componentName: 'Project'
//     },
//     {
//       name: '环境管理',
//       componentName: 'LoginEnv'
//     }]
//   }, {
//     name: 'VirtualAsset',
//     id: 'VA',
//     sub: [{
//       name: 'VA列表',
//       componentName: 'VAView'
//     }]
//   }]

const menuBarList = [{
  name: '接口',
  id: 'interface',
  sub: [{
    name: '工程目录',
    componentName: 'Project'
  },
  {
    name: '环境管理',
    componentName: 'LoginEnv'
  }]
}, {
  name: 'VirtualAsset',
  id: 'VA',
  sub: [{
    name: 'VA列表',
    componentName: 'VAView'
  }]
}]

const backEndUrl = "http://localhost:5000/"
const backEndPath = {
  getProject:"getProjects",
  getAllLoginEnv:"getAllLoginEnv"
}

  export default
  {
    menuBarList,
    backEndUrl,
    backEndPath
  }