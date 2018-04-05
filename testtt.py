# -*- coding: utf-8 -*-

import time
import TencentYoutuyun

appid = '10124755'
secret_id = 'AKIDznMgnf5BakvvrZ9OWV0LWr1xe8OQuoAH'
secret_key = '1pSSGxQdaIlyvd5KL8h291g6IFyTkoeG'
userid= '327359574'

#end_point = TencentYoutuyun.conf.API_TENCENTYUN_END_POINT  // 腾讯云
#end_point = TencentYoutuyun.conf.API_YOUTU_VIP_END_POINT   // 人脸核身服务(需联系腾讯优图商务开通权限，否则无法使用)
end_point = 'TencentYoutuyun.conf.API_YOUTU_END_POINT'


youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)

ret = youtu.FaceCompare('you_path_one.jpg','you_path_two.jpg')
print(ret)