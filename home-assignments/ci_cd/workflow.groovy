node ('ops_school_dynamic_slave') {
   echo "Start!"

   stage('Checkout') {
       dir('Solution1') {
           git url: 'https://github.com/AviadP/opsschool3-coding.git'
       }
    sh '''
          pwd
          echo ls
          cd Solution1
          python3 home-assignments/session1/solution1.py --input "home-assignments/session1/input.json"
   '''
   }

   echo "Done!"
}