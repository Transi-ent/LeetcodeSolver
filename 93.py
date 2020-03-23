"""
TODO: 使用回溯法，本质上就是深度优先搜索，从初始条件出发，不断地鬼搜索满足要求的所有答案
，每次都先找到一个完整的答案，在从头变换初始条件搜索下一个答案
"""
class Solution:
    def restoreIpAddresses(self, s: str):

        res = list()
        self._restoreIpAddresses(s, 0, '', res, 0)
        return res


    def _restoreIpAddresses(self, s: str,
                            index: int,
                            tmp_res: str,
                            res: list,
                            times: int):
        if index>=len(s):
            return
        if times==3:
            if 0<len(s[index:])<=3 and int(s[index:])<256:
                tmp_res+=s[index:]
                lyst = tmp_res.split('.')
                for item in lyst:
                    if len(item)>1 and item.startswith('0'):
                        return
                res.append(tmp_res)

            return

        for i in range(1,4):
            tmp_s = s[index: index+i]
            #print(tmp_s, len(tmp_s),'[index, index+i]: [',index, index+i,']')
            if int(tmp_s)<256:
                self._restoreIpAddresses(s, index+i, tmp_res+tmp_s+'.', res, times+1)

    def restoreIpAddresses2(self, s: str) -> list:
        """
        输入一个字符串，将该字符串切分成4块，每一个转变成 int 型整数后都在 0~255之间
        :param s:
        :return:
        """
        if len(s)<4:
            return []
        ips = []
        ips = self.findIpAddresses(s, 0, ips, 0, '')
        #print(ips)
        ips = [em[1:] for em in ips]
        return ips

    def findIpAddresses(self,s:str, index:int, ips:list, n_seg:int, seg: str)->list:
        """
        :param s: 函数输入，字符串；
        :param index: 输入字符串当前该处理的位置索引；
        :param ips: 最终要返回的 IP 地址列表；
        :param n_sge: 已经完成的 IP 地址块数；
        :return:
        """
        if n_seg==3:
            remaint = s[index:]
            if remaint and int(remaint)<=255:
                if (len(remaint)>1 and remaint[0]!='0') or len(remaint)==1:
                    seg += '.'
                    seg += remaint
                    ips.append(seg)
            return ips

        for i in range(1, 4):
            num = s[index: index+i]
            print('index: ',index, "seg: ",seg, 'num: ',num)
            if num and int(num)<=255 :
                if (len(num)>1 and num[0]!='0') or (len(num)==1 ):
                    self.findIpAddresses(s, index+i, ips, n_seg+1, seg+'.'+num)
        return ips





res = Solution().restoreIpAddresses2("0000")
print(res)
