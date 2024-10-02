def solution(root):

    q = []
    q.append((root, 0))
    curindex = 0
    curlevel = []
    answer = []
    while q:
        node, idx = q.pop(0)
        if idx == curindex:
            if node.val:
                curlevel.append(node.val)
                q.append((node.left, idx + 1))
                q.append((node.right, idx + 1))
            else:
                curlevel.append(None)


        if idx != curindex:
            answer.append(curlevel)
            curlevel = []
            curindex += 1
            if node.val:
                curlevel.append(node.val)
                q.append((node.left, idx + 1))
                q.append((node.right, idx + 1))
            else:
                curlevel.append(None)

    answer.append(curlevel)
    return answer


