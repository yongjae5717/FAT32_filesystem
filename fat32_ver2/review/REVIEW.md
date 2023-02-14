# Code Review

## Buffer i/o
 - 모든 코드에서 buffered i/o를 못하고 있습니다.
 - 우리가 처리해야할 데이터가 file로 주어질 수 있지만
   remote network의 socket, mobile phone, raw device 등등 무엇이 될 수 있기 때문에
   sector / cluster 단위로 buffer를 읽어오는 코드를 만들지 않으면 입력에 대해서
   동일한 일을 하는 함수를 각각 만들어야 합니다.

## coding style
 - 클래스 이름에 일관성이 없어요
   1. class Node, FileManage
   2. class cluster_rule, dir_reppare

## Code Structure
 - 아래처럼 각 레이어를 나누어 역할을 나눈 클래스를 만들어야
   각 클래스는 자신과 관계가 있는 최소한의 클래스와만 의존성을 가질 수 있습니다.

 - layer 1
   class BootRecord, class FatTable, class DirectoryEntry

 - layer 2
   class Node, 
   class NodeStream 
         DirectoryEntry 의 first cluster no에서 모든 cluster no을 읽은 후 read/seek 구현)

 - layer 3
   class Fat, 

## endian.py
 - 입력은 byte arary, 출력은 정수가 되어야 합니다. 
   (코드 내 두 함수는 문자열을 반환, 코드를 봤을때 이 두함수를 왜 사용하는지 이해하지 못한 것 같아요)
 - python에서는 struct module의 unpack을 써서 구현하면, 다시 int()로 변환하는 함수를 사용하지 않아도 됩니다.
   (review/byte_buffer2.py의 def get_uint2_le 참고)

## file_manage.py
 - 수업시간에는 DirectoryEntry 혹은 iNode로 공부를 했습니다.
 - 변수명에서 manager, item 등등은 사용을 지양합니다.
 - 이 클래스에서 first_cluster_no를 다 다루어야 합니다.
   cluster_no 처리를 class_prepare에서 사용하고 있네요.


## dir_prepare.py
 - 객체의 이름이 적절해보이지 않습니다.
 - file_manage와 fat 클래스에 위 코드가 move refactoring될 수 있습니다.

## dir_file_read.py
 - 객체의 role이 이미 다른 코드와의 관계에서 많이 섞여버려서
   생성자에 다른 모든 객체의 타입정보가 다 섞여 들어왔네요.

## cluster_chain, cluster_rule
 - 두 클래스는 하나로 합쳐질 수 있습니다.
 