import axios from 'axios'
import global from '@/config/global'

function getList(collectionName,searchName){
    var res = axios.get(global.backEndUrl + global.backEndPath["getList"], {
        params: {
            name: searchName,
            collectionName: collectionName
        }
    })
    return res
}

export default{
    getList
} 