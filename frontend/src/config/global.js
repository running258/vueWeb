
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
  getProject:"getProjects",   //获取所有项目
  insertNewProject:"insertNewProject",  //新建项目
  getProjectAndIntersByProjectName:"getProjectAndIntersByProjectName",  //项目中添加新接口
  interInfoById:"interInfoById",  //根据id查看接口详情
  runSingleInter:"runSingleInter",  //单接口执行
  saveInterAndUpdateProject:"saveInterAndUpdateProject",  //项目内保存接口
  updateLoginEnv:"updateLoginEnv",  //环境保存
  getAllLoginEnv:"getAllLoginEnv",  //获取所有环境
}

  export default
  {
    menuBarList,
    backEndUrl,
    backEndPath
  }